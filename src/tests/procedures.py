from src.etl.pipelines.build_open_ar import build_open_ar

try:
    build_open_ar()
    print('Success!')
except Exception as e:
    print(e)

