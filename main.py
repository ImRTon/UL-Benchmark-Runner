import argparse
import os
import time

from pathlib import Path

from config import ul_3dmarks, ul_procyons

def get_args():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-i', '--dir_path', type=str, required=True, help='Benchmarks parent directory.')
    parser.add_argument('-d', '--device', type=str, required=True, help='cuda or xpu')
    parser.add_argument('-o', '--output', type=str, required=True, help='Output dir path')
    parser.add_argument('--shutdown', action='store_true', help='Shutdown the computer after complete the benchmarks')
    return parser.parse_args()

def main():
    args = get_args()
    output_dir = Path(args.output)

    # 3DMark
    for benchmark_name in ul_3dmarks:
        output_path = output_dir / f"{benchmark_name.split('.')[0]}.3dmark-result"
        xml_output_path = output_dir / f"{benchmark_name.split('.')[0]}.xml"
        os.system(f'{args.dir_path}\\3DMark\\3DMarkCmd.exe --definition={benchmark_name} '
                  f'--result="{output_path.absolute()}" --export="{xml_output_path.absolute()}"')
        time.sleep(5*60)

    # Procyon
    for benchmark_name in ul_procyons[args.device]:
        output_path = output_dir / f"{benchmark_name.split('/')[-1].split('.')[0]}.procyon-result"
        csv_output_path = output_dir / f"{benchmark_name.split('/')[-1].split('.')[0]}.csv"
        os.system(f'{args.dir_path}\\Procyon\\ProcyonCmd.exe --definition={benchmark_name} '
                  f'--result="{output_path.absolute()}" --export-csv "{csv_output_path.absolute()}"')
        time.sleep(5*60)

    if args.shutdown:
        os.system("shutdown /s /t 1") # Shutdown the computer

if __name__ == '__main__':
    main()