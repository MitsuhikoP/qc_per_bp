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
python3 qc_per_bp.py [-t num_threads] [-p output_prefix] [-s pdf_width] *fastq[.gz]
```
