from app.common.model import Base, id_key
from sqlalchemy.orm import Mapped, mapped_column, relationship

import sqlalchemy as sa

from app.models.db import uuid4_str


class User(Base):
    """用户表"""

    __tablename__ = 'kd_files_own'

    id: Mapped[id_key] = mapped_column(init=False)
    tid: Mapped[int] = mapped_column(comment='tid')
    uid: Mapped[int] = mapped_column(comment='uid')
    file_name: Mapped[str] = mapped_column(sa.String(20), unique=True, index=True, comment='文件名')
    file_ext: Mapped[str] = mapped_column(sa.String(20), comment='文件扩展名')
    mtime: Mapped[int] = mapped_column(comment='新建时间')
