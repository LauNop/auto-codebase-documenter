from my_auto_codebase_documenter.AutoCodebaseDocumenter import AutoCodebaseDocumenter

from env import envVar as V

ignore_folders = ["tests"]
unwanted_files = ["setup.py","__init__.py", "documenter.py", "format_code.py","auto_documenter.py"]
documenter = AutoCodebaseDocumenter(openai_org_id=V.openai_org_id, openai_api_key=V.openai_api_key,
                                    ignore_folders=ignore_folders, unwanted_files=unwanted_files, gpt_model="gpt-4", language='fr')
files = documenter._get_file_paths()
print(len(files))
print(files)
documenter.process_all_files()
