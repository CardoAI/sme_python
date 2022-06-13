from dataclasses import dataclass
from typing import Callable, Optional


@dataclass
class APIConfig:
    host: str
    username: str
    password: str


@dataclass
class S3Config:
    s3_access_key_id: str
    s3_secret_access_key: str
    s3_bucket_name: str
    s3_region_name: str
    s3_presigned_url_expiration_time: int = 3600
    file_name_generator: Optional[Callable] = None
