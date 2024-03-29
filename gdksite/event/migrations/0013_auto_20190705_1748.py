# Generated by Django 2.2.1 on 2019-07-05 07:48

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0012_auto_20181221_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventpage',
            name='age_policy',
            field=models.PositiveIntegerField(default=3, validators=[django.core.validators.MaxValueValidator(18), django.core.validators.MinValueValidator(0)], verbose_name='Возрастное ограничение'),
        ),
        migrations.AlterField(
            model_name='eventpage',
            name='body',
            field=wagtail.core.fields.StreamField([('heading_block', wagtail.core.blocks.StructBlock([('heading_text', wagtail.core.blocks.CharBlock(classname='title', required=True)), ('size', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4')], required=False))])), ('paragraph_block', wagtail.core.blocks.RichTextBlock(icon='fa-paragraph', template='blocks/paragraph_block.html')), ('image_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False))])), ('block_quote', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.TextBlock()), ('attribute_name', wagtail.core.blocks.CharBlock(blank=True, label='e.g. Mary Berry', required=False))])), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='fa-s15', template='blocks/embed_block.html')), ('event_block', wagtail.core.blocks.StructBlock([('age_policy', wagtail.core.blocks.IntegerBlock(label='Возрастной контроль', max_value=18, min_value=0)), ('event_time', wagtail.core.blocks.DateTimeBlock(label='Дата события')), ('mesto_sobytiya', wagtail.core.blocks.CharBlock(blank=True, label='Место события', required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(label='Изображение', required=True))], help_text='Укажите дату и время события', icon='fa-calendar', template='blocks/event_block.html'))], blank=True, null=True, verbose_name='Основное описание'),
        ),
        migrations.AlterField(
            model_name='eventpage',
            name='event_date',
            field=models.DateField(null=True, verbose_name='Дата проведения мероприятия'),
        ),
        migrations.AlterField(
            model_name='eventpage',
            name='event_time',
            field=models.TimeField(null=True, verbose_name='Время проведения мероприятия'),
        ),
        migrations.AlterField(
            model_name='eventpage',
            name='image',
            field=models.ForeignKey(blank=True, help_text='Landscape mode only; horizontal width between 1000px and 3000px.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image', verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='eventpage',
            name='introduction',
            field=models.TextField(blank=True, help_text='Text to describe the page', verbose_name='Место проведения'),
        ),
        migrations.AlterField(
            model_name='eventpage',
            name='subtitle',
            field=models.CharField(blank=True, max_length=255, verbose_name='Краткое описание'),
        ),
    ]
