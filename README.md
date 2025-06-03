# UL Benchmark Runner
This is a simple benchmark runner for the UL Benchmarks, ex: Procyon, 3DMark, PCMark, etc.  

## Usage
```bash
python main.py -i <UL Parent Dir Path> -d <Device Name> -o <Output Dir Path> --ul_3dmark --ul_pcmark --ul_procyon --shutdown
```
* `-i` or `--input` : Path to the UL Parent Directory. The path must be enclosed in double quotes (e.g., "C:\Your Path")  
* `-d` or `--device` : Device Name, can be multiple  
* `-o` or `--output` : Output Directory Path  
* `-s` or `--sleep` : Idel time in seconds between benchmarks
* `--ul_3dmark` : Run 3DMark Benchmark  
* `--ul_pcmark` : Run PCMark Benchmark  
* `--ul_procyon` : Run Procyon Benchmark  
* `--shutdown` : Shutdown the system after the benchmark is completed  