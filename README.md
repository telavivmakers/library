# TAMI Library

Library barcode scanning and indexing

## Usage

### Collect Barcodes

Plug in your USB barcode scanner, then:

```bash
$ python collector.py
```

All scans are appended to `barcode_scan.log`.

### Process Barcodes

```bash
$ python process.py barcode_scan.log
```
