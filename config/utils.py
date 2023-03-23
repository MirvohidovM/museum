import sys, os, re, string, random
from django.templatetags.static import static
from django.utils.functional import lazy
from django.utils.text import slugify
from slugify import slugify as slug_translate
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import Image
from io import BytesIO
static_lazy = lazy(static, str)


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_slug_generator(instance, title, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(title, allow_unicode=True)
        slug = slug_translate(slug)
    title = ''.join(re.split(r'[‘.;!?,\']', title))
    Klass = instance.__class__
    max_length = Klass._meta.get_field('slug').max_length
    slug = slug[:max_length]
    qs_exists = Klass.objects.filter(slug=slug).exists()

    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
            slug=slug[:max_length - 5], randstr=random_string_generator(size=4))

        return unique_slug_generator(instance, title, new_slug=new_slug)
    return slug


def compressImage(image):
    try:
        im = Image.open(image)
        im.verify()
    except Exception:
        return None

    im = Image.open(image)
    extension = im.format.lower()
    im_io = BytesIO()

    if extension == 'jpg' or extension == 'jpeg':
        im.save(im_io, format='JPEG', optimize=True, quality=50)
        jpg = InMemoryUploadedFile(im_io, 'ImageField', "%s.jpeg" % image.name.split(
            '.')[0], 'image/jpeg', sys.getsizeof(image), None)
        return jpg
    elif extension == 'png':
        im.save(im_io, format='PNG', optimize=True, quality=50)
        png = InMemoryUploadedFile(im_io, 'ImageField', "%s.PNG" % image.name.split(
            '.')[0], 'image/png', sys.getsizeof(image), None)
        return png
    elif extension == 'webp':
        im.save(im_io, format='WEBP', optimize=True, quality=50)
        webp = InMemoryUploadedFile(im_io, 'ImageField', "%s.webp" % image.name.split(
            '.')[0], 'image/webp', sys.getsizeof(image), None)
        return webp


def validate_file_extension(video):
    ext = os.path.splitext(video.name)[1]  # [0] returns path+filename
    valid_extensions = ['.mp3', '.acc', '.flac', '.alac', '.wav', '.aiff', '.dsd', '.pcm']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Iltimos audio fayl tanlang.')


def imagefile_validation_exception(value):
    ext = os.path.splitext(value.name)[-1]
    valid_exceptions = ['.jpg', '.jpeg', '.png', '.svg']
    if not ext.lower() in valid_exceptions:
        raise ValidationError('Unsupported file extension.')
