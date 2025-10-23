import logging
import os
import tempfile
from typing import Tuple, Iterator

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class CSVFileSplitter:
    def __init__(self, chunk_size: int):
        """Initialize the CSV file splitter.

        Args:
            chunk_size (int): Target size for each chunk in bytes
        """
        self.chunk_size = chunk_size
        self.temp_dir = None

    def __enter__(self):
        """Create temporary directory when entering context."""
        self.temp_dir = tempfile.mkdtemp(prefix='csv_split_')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Clean up temporary directory when exiting context."""
        if self.temp_dir and os.path.exists(self.temp_dir):
            for file in os.listdir(self.temp_dir):
                try:
                    os.remove(os.path.join(self.temp_dir, file))
                except Exception as e:
                    logger.warning(f"Failed to remove temporary file {file}: {e}")
            try:
                os.rmdir(self.temp_dir)
            except Exception as e:
                logger.warning(f"Failed to remove temporary directory: {e}")

    def split_file(self, file_path: str, num_parts: int) -> Iterator[Tuple[str, int]]:
        """Split a CSV file into parts while preserving CSV structure.
        Each part is saved as a temporary file.

        Args:
            file_path (str): Path to the CSV file
            num_parts (int): Number of parts to split into

        Yields:
            Tuple[str, int]: Tuple of (temp_file_path, part_number)
        """
        if not self.temp_dir:
            raise RuntimeError("CSVFileSplitter must be used as a context manager")

        current_part = 1
        current_size = 0
        current_file = None
        current_writer = None

        try:
            with open(file_path, 'r', newline='') as f:
                # Read header
                header = next(f)
                header_size = len(header.encode('utf-8'))

                # Create first part file
                current_file = self._create_temp_file(current_part)
                current_writer = open(current_file, 'w', newline='')
                current_writer.write(header)
                current_size = header_size

                # Read rows
                for row in f:
                    row_size = len(row.encode('utf-8'))

                    # If adding this row would exceed chunk size and we're not on the last part,
                    # close current file and start a new one
                    if current_size + row_size > self.chunk_size and current_part < num_parts:
                        current_writer.close()
                        yield current_file, current_part

                        current_part += 1
                        current_file = self._create_temp_file(current_part)
                        current_writer = open(current_file, 'w', newline='')
                        current_size = header_size

                    current_writer.write(row)
                    current_size += row_size

                # Close the last file if it exists
                if current_writer:
                    current_writer.close()
                    yield current_file, current_part

        except Exception as e:
            # Clean up in case of error
            if current_writer:
                current_writer.close()
            if current_file and os.path.exists(current_file):
                os.remove(current_file)
            raise e

    def _create_temp_file(self, part_number: int) -> str:
        """Create a temporary file for a part.

        Args:
            part_number (int): The part number

        Returns:
            str: Path to the created temporary file
        """
        temp_file = os.path.join(self.temp_dir, f'part_{part_number}.csv')
        return temp_file