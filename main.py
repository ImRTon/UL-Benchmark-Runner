import argparse
import subprocess
import time

from pathlib import Path

from config import ul_3dmarks, ul_procyons

def get_args():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-i', '--dir_path', type=str, required=True, help='Benchmarks parent directory.')
    parser.add_argument('-d', '--device', type=str, required=True, help='cuda or xpu')
    parser.add_argument('-o', '--output', type=str, required=True, help='Output dir path')
    parser.add_argument('-s', '--sleep', type=int, default=5*60, help='Sleep time between benchmarks')
    parser.add_argument('--ul_3dmark', action='store_true', help='Run 3DMark benchmarks')
    parser.add_argument('--ul_procyon', action='store_true', help='Run Procyon benchmarks')
    parser.add_argument('--shutdown', action='store_true', help='Shutdown the computer after complete the benchmarks')
    return parser.parse_args()

def main():
    args = get_args()
    output_dir = Path(args.output)

    # 3DMark
    if args.ul_3dmark:
        for benchmark_name in ul_3dmarks:
            output_path = output_dir / f"{benchmark_name.split('.')[0]}.3dmark-result"
            xml_output_path = output_dir / f"{benchmark_name.split('.')[0]}.xml"

            subprocess.run([
                f'{args.dir_path}\\3DMark\\3DMarkCmd.exe', 
                f'--definition={benchmark_name}', 
                f'--out={output_path.absolute()}', 
                f'--export={xml_output_path.absolute()}'
            ])

            time.sleep(args.sleep)

    # Procyon
    if args.ul_procyon:
        for benchmark_name in ul_procyons[args.device]:
            output_path = output_dir / f"{benchmark_name.split('/')[-1].split('.')[0]}.procyon-result"
            csv_output_path = output_dir / f"{benchmark_name.split('/')[-1].split('.')[0]}.csv"

            subprocess.run([
                f'{args.dir_path}\\Procyon\\ProcyonCmd.exe', 
                f'--definition={Path.cwd().absolute()}\\{benchmark_name}', 
                f'--result="{output_path.absolute()}"', 
                f'--export-csv="{csv_output_path.absolute()}"'
            ])
            time.sleep(args.sleep)

    if args.shutdown:
        os.system("shutdown /s /t 1") # Shutdown the computer

if __name__ == '__main__':
    main()