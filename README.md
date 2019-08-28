# qc_per_bp
per-base quality check for fastq files

## Dependency
- python3
- biopython
- joblib
- R
- ggplot2

If you don't install `ggplot2`, they are automatically installed.


```
pip3 install biopython, joblib
```

## USAGE
```
python3 qc_per_bp.py [-t num_threads] [-p output_prefix] [-s pdf_width] input1.fastq[.gz]...
```
positional arguments:
  str         fastq files

optional arguments:
  -h, --help  show this help message and exit
  -t int      num threads (default=2)
  -p str      output prefix (default=quality_check)
  -s float    pdf width (default=10)
  -m int      minimum num reads using output graph. (default=0: all samples
              are calculated.)
