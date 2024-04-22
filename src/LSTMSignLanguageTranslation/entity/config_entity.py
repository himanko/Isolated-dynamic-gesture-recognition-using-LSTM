from dataclasses import dataclass
from pathlib import Path
import tensorflow as tf


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path