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
    return parser.parse_args()

def main():
    args = get_args()
    output_dir = Path(args.output)

    # 3DMark
    for benchmark_name in ul_3dmarks:
        output_path = output_dir / f"{benchmark_name.split('.')[0]}.3dmdef"
        os.system(f"{args.dir_path}\\\\3DMarkCmd.exe --definition={benchmark_name} --result={output_path.absolute()}")
        time.sleep(5*60)

    # Procyon
    for benchmark_name in ul_procyons[args.device]:
        output_path = output_dir / f"{benchmark_name.split('/')[-1]}"
        os.system(f"{args.dir_path}\\\\ProcyonCmd.exe --definition={benchmark_name} --result={output_path.absolute()}")
        time.sleep(5*60)

if __name__ == '__main__':
    main()