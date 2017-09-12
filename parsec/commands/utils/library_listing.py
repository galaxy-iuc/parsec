import click
from parsec.cli import pass_context
from parsec.decorators import custom_exception, dict_output


@click.command('library_listing')
@click.argument("library_id", type=str, required=True)
@pass_context
@custom_exception
@dict_output
def cli(ctx, library_id):
    """
    Recursively descend through a directory and output information about files
    in these directories. This essentially is an iterator over all files in a
    library dataset. Each file object includes the parent folder's metadata
    attached to it allowing for arbitrary transformations (data de-normalized
    for your convenience)::

        {
            "_folder": {
                "can_add_library_item": true,
                "can_modify_folder": true,
                "folder_description": "Files in VCF format",
                "folder_name": "Variants",
                "full_path": [
                    [
                    "F03501d7626bd192f",
                    "Genomes + annotations"
                    ],
                    [
                    "F76fc6a61d2847f9c",
                    "Variants"
                    ]
                ],
                "parent_library_id": "1cd8e2f6b131e891"
            },
            "_folder_ids": [
                "F03501d7626bd192f",
                "F76fc6a61d2847f9c"
            ],
            "_folder_names": [
                "Genomes + annotations",
                "Variants"
            ],
            "_folder_path": "Genomes + annotations/Variants",
            "can_manage": true,
            "create_time": "2014-03-19 04:08 PM",
            "date_uploaded": "2014-03-19T16:08:26.000068",
            "deleted": false,
            "file_ext": "vcf",
            "file_size": "86.0 MB",
            "id": "ac6367e9a88360c8",
            "is_private": false,
            "is_unrestricted": true,
            "name": "Mills_and_1000G_gold_standard.indels.hg19.vcf",
            "type": "file",
            "update_time": "2014-03-19 04:08 PM"
        }

    """
    lib = ctx.gi.libraries.show_library(library_id)
    # print('\t'.join(['Folder', 'Name', 'Uploaded', 'File Extension', 'File Size']))
    results = []

    def handle_folders(folder_id):
        folder = ctx.gi.folders.show_folder(folder_id, contents=True)
        for item in folder['folder_contents']:
            if item['type'] != 'folder':
                tmp = {
                    '_folder': folder['metadata'],
                    '_folder_ids': [x[0] for x in folder['metadata']['full_path']],
                    '_folder_names': [x[1] for x in folder['metadata']['full_path']],
                    '_folder_path': '/'.join([x[1] for x in folder['metadata']['full_path']]),
                }
                tmp.update(item)
                results.append(tmp)
            if item['type'] == 'folder':
                handle_folders(item['id'])

    handle_folders(lib['root_folder_id'])
    return results
