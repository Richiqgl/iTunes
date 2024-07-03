
from dataclasses import dataclass
@dataclass
class Album():
    AlbumId:int
    Title:str
    ArtistId:int
    totD:int

    def __hash__(self):
        return hash(self.AlbumId)

    def __str__(self):
        return f"{self.AlbumId}----{self.Title}-----{self.AlbumId}-----{self.totD}"

    def __eq__(self, other):
        return self.AlbumId==other.AlbumId