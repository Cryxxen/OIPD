from utils.models import BaseModel


class Club(BaseModel):
    class Meta:
        verbose_name = "Клуб"
        verbose_name_plural = "Клубы мира"
        ordering = ("-id",)

    def __str__(self):
        return f"{self.id}---{self.title_ru}"
