from django.core.management.base import BaseCommand
from django.utils.text import slugify
from django.utils.translation import gettext as _
from posts.models import Post, Tag
from users.models import User


class Command(BaseCommand):
    help = "My shiny new management command."

    def add_arguments(self, parser):
        parser.add_argument(
            "number_posts",
            type=int,
            help=_("Informs the number of posts to be created"),
        )

    def handle(self, *args, **options):
        number_posts = options.get("number_posts", 12)
        for number_post in range(1, number_posts + 1):
            title = "Post de Numero {}".format(number_post)
            slug = slugify(title)
            author = User.objects.all().first()
            excerpt = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin posuere sodales purus sed semper.\
                In est dui, lacinia sed ipsum sed, feugiat venenatis ex. Praesent dapibus tortor a mollis vestibulum. Cras eros justo,\
                faucibus ac molestie nec, aliquam at nunc. Fusce enim leo, auctor sit amet libero sed, congue rhoncus tellus. Suspendisse \
                porttitor enim dapibus lectus vulputate suscipit. Proin luctus in metus at luctus. Pellentesque at turpis justo.\
                Donec scelerisque sodales justo, ut consectetur nunc tincidunt quis. Donec blandit urna ac ante interdum dapibus."
            content = "<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin posuere sodales purus sed semper. In est dui, lacinia sed ipsum sed, feugiat venenatis ex. Praesent dapibus tortor a mollis vestibulum. Cras eros justo, faucibus ac molestie nec, aliquam at nunc. Fusce enim leo, auctor sit amet libero sed, congue rhoncus tellus. Suspendisse porttitor enim dapibus lectus vulputate suscipit. Proin luctus in metus at luctus. Pellentesque at turpis justo. Donec scelerisque sodales justo, ut consectetur nunc tincidunt quis. Donec blandit urna ac ante interdum dapibus.</p>\
                <p>Aliquam volutpat nulla est, in rhoncus orci porttitor nec. In ullamcorper, nunc a sagittis rhoncus, sem magna condimentum elit, ut auctor neque ante in leo. Aliquam erat volutpat. Phasellus lacus mi, vestibulum eget molestie eget, varius at neque. In ac aliquam ligula. Quisque orci sem, venenatis nec risus et, viverra gravida ligula. Sed et purus sit amet felis vestibulum convallis vel vel orci. Etiam efficitur sem id nisi imperdiet, sit amet sollicitudin tortor vestibulum. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. In rutrum iaculis ornare. Nam sit amet urna lorem. Maecenas a neque vel nunc pellentesque laoreet. Etiam semper felis mattis diam congue varius.</p>\
                <p>Curabitur enim dolor, sagittis ac fermentum et, tristique quis eros. Vivamus ligula magna, ullamcorper sit amet dui et, bibendum dignissim quam. Aliquam risus erat, lobortis vitae ultricies dignissim, bibendum nec urna. Sed vulputate elit felis, condimentum tincidunt ex placerat non. Nunc ullamcorper, arcu eget fringilla aliquam, est diam bibendum felis, ut venenatis odio enim at leo. Quisque nulla urna, semper et. </p>"
            tags = Tag.objects.all()
            is_active = True

            post = Post.objects.create(
                title=title,
                slug=slug,
                author=author,
                excerpt=excerpt,
                content=content,
                is_active=is_active,
            )
            for tag in tags:
                post.tags.add(tag.id)
            post.save()
