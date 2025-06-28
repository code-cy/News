from django.db import models

class TopArticle(models.Model):
    source_id = models.CharField(max_length=100, null=True, blank=True)
    source_name = models.CharField(max_length=255)
    author = models.CharField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=500)
    description = models.TextField(null=True, blank=True)
    url = models.URLField()
    url_to_image = models.URLField(null=True, blank=True)
    published_at = models.DateTimeField()
    content = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title









"""
----------------------Test data -------------------------


{
    "source": {
    "id": "associated-press",
    "name": "Associated Press"
    },
    "author": null,
    "title": "Trump says US has signed a deal with China on trade, without giving details",
    "description": "U.S. President Donald Trump says the U.S. has signed an agreement with China on trade and expects to soon have a deal with India. Commerce Secretary Howard Lutnick told Bloomberg TV that the deal was signed earlier this week, but he gave no details. He said T…",
    "url": "https://apnews.com/article/china-trade-earths-tariffs-trump-463ae8d6ccba15b56c7d4d31d3fc42a1",
    "urlToImage": "https://dims.apnews.com/dims4/default/3343bf3/2147483647/strip/true/crop/3943x2218+0+207/resize/1440x810!/quality/90/?url=https%3A%2F%2Fassets.apnews.com%2Ffb%2F6f%2Fb6f769108f2aab05f77edb1e49cb%2Fecf14e435f3d4343b20a557e7e101371",
    "publishedAt": "2025-06-27T06:04:51Z",
    "content": "BANGKOK (AP) The U.S. and China have signed an agreement on trade, President Donald Trump said, adding he expects to soon have a deal with India. \r\nCommerce Secretary Howard Lutnick told Bloomberg TV… [+1136 chars]"
},

"""