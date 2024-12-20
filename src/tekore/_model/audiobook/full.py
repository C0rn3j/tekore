from __future__ import annotations

from ..chapter import SimpleChapterPaging
from .base import Audiobook


class FullAudiobook(Audiobook):
    """Complete audiobook object."""

    chapters: SimpleChapterPaging
    is_playable: bool | None = None
