from django.core.management.base import BaseCommand

from wagtail.wagtailcore.models import Page

from akllt.dataimport.news import import_news
from akllt.news.models import NewsStory


class Command(BaseCommand):
    args = '<directory name>'
    help = 'Imports data from old akl.lt website'

    def handle(self, news_folder, *args, **options):
        news_count = 0
        root = Page.get_first_root_node()
        if root is None:
            root = Page.add_root(title='Root page')

        news = import_news(news_folder)
        for news_story in news:
            root.add_child(instance=NewsStory(
                title=news_story['title'],
                date=news_story['date'],
                blurb=news_story['blurb'],
                body=news_story['body'],
            ))
            news_count += 1

        self.stdout.write('Successfully imported %d news items\n' % news_count)
