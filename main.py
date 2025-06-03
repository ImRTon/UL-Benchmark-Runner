import argparse
import subprocess
import time

from pathlib import Path

from config import ul_3dmarks, ul_pcmarks, ul_procyons

def get_args():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-i', '--dir_path', type=str, required=True, help='Benchmarks parent directory.')
    parser.add_argument('-d', '--device', type=str, required=True, nargs='+', choices=['cuda', 'xpu', 'npu'], 
                        help='devices for ai benchmarks')
    parser.add_argument('-o', '--output', type=str, required=True, help='Output dir path')
    parser.add_argument('-s', '--sleep', type=int, default=5*60, help='Sleep time between benchmarks')
    parser.add_argument('--ul_3dmark', action='store_true', help='Run 3DMark benchmarks')
    parser.add_argument('--ul_pcmark', action='store_true', help='Run PCMark benchmarks')
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

    # PCMark
    if args.ul_pcmark:
        for benchmark_name in ul_pcmarks:
            output_path = output_dir / f"{benchmark_name.split('.')[0]}.pcmark-result"
            xml_output_path = output_dir / f"{benchmark_name.split('.')[0]}.xml"

            subprocess.run([
                f'{args.dir_path}\\PCMark 10\\PCMark10Cmd.exe', 
                f'--definition={benchmark_name}', 
                f'--out={output_path.absolute()}', 
                f'--export={xml_output_path.absolute()}'
            ])

            time.sleep(args.sleep)

    # Procyon
    if args.ul_procyon:
        benchmarks = []
        for device in args.device:
            benchmarks.extend(ul_procyons[device])  # Add benchmarks for specified devices
        for benchmark_name in benchmarks:
            output_path = output_dir / f"{benchmark_name.split('/')[-1].split('.')[0]}.procyon-result"
            csv_output_path = output_dir / f"{benchmark_name.split('/')[-1].split('.')[0]}.csv"

            subprocess.run([
                f'{args.dir_path}\\Procyon\\ProcyonCmd.exe', 
                f'--definition={Path.cwd().absolute()}\\{benchmark_name}', 
                f'--out="{output_path.absolute()}"', 
                f'--export-csv="{csv_output_path.absolute()}"'
            ])
            time.sleep(args.sleep)

    if args.shutdown:
        subprocess.run(["shutdown", "/s", "/t", "1"]) # Shutdown the computer

if __name__ == '__main__':
    main()