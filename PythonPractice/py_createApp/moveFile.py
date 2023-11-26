import os
import shutil

def organize_files(directory):
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            # ファイル名と拡張子を分割
            name, ext = os.path.splitext(filename)
            # 先頭の「_」までの命名を取得
            prefix = name.split('_')[0]
            # 新しいフォルダ名を設定（拡張子またはプレフィックス）
            new_dir = ext[1:] if ext else prefix
            # 新しいフォルダのパスを設定
            new_dir_path = os.path.join(directory, new_dir)
            # 新しいフォルダを作成（既に存在する場合は作成しない）
            os.makedirs(new_dir_path, exist_ok=True)
            # ファイルを新しいフォルダに移動
            shutil.move(os.path.join(directory, filename), os.path.join(new_dir_path, filename))

# フォルダを指定して関数を呼び出す
organize_files('C:\\Users\\0719AM\\Documents\\test')
