# High-Level Clients for CleverMaps Data Operations

A Python library providing high-level client interfaces for common CleverMaps operations.

## Overview

This package simplifies interaction with CleverMaps projects by providing intuitive, high-level methods that handle complex workflows behind the scenes. It's built on top of the CleverMaps Python OpenAPI SDK.
## Features

- **Data Dumping**: Export datasets from CleverMaps projects to CSV files
- **Data Loading**: Upload CSV files to CleverMaps projects with automatic handling of:
  - Single-part uploads for small files
  - Multipart uploads with GZIP compression for large files
  - Automatic file splitting while preserving CSV structure

## Installation

```bash
pip install cm-python-openapi-sdk
```
