import click
from parsec.cli import pass_context
from parsec.decorators import custom_exception


@click.command('library_listing')
@click.argument("library_id", type=str, required=True)
@pass_context
@custom_exception
def cli(ctx, library_id):
    lib = ctx.gi.libraries.show_library(library_id)
    print('\t'.join(['Folder', 'Name', 'Uploaded', 'File Extension', 'File Size']))

    def handle_folders(folder_id):
        folder = ctx.gi.folders.show_folder(folder_id, contents=True)

        current_path = '/'.join([x[1] for x in folder['metadata']['full_path']])
        for item in folder['folder_contents']:
            if item['type'] != 'folder':
                print('\t'.join([
                    current_path,
                    item['name'],
                    item['date_uploaded'],
                    item['file_ext'],
                    item['file_size'],
                ]))
            if item['type'] == 'folder':
                handle_folders(item['id'])

    handle_folders(lib['root_folder_id'])
