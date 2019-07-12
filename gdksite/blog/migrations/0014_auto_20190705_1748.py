# Generated by Django 2.2.1 on 2019-07-05 07:48

from django.db import migrations, models
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20181220_0518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='body',
            field=wagtail.core.fields.StreamField([('heading_block', wagtail.core.blocks.StructBlock([('heading_text', wagtail.core.blocks.CharBlock(classname='title', required=True)), ('size', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4')], required=False))])), ('paragraph_block', wagtail.core.blocks.RichTextBlock(icon='fa-paragraph', template='blocks/paragraph_block.html')), ('image_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False))])), ('block_quote', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.TextBlock()), ('attribute_name', wagtail.core.blocks.CharBlock(blank=True, label='e.g. Mary Berry', required=False))])), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='fa-s15', template='blocks/embed_block.html')), ('event_block', wagtail.core.blocks.StructBlock([('age_policy', wagtail.core.blocks.IntegerBlock(label='Возрастной контроль', max_value=18, min_value=0)), ('event_time', wagtail.core.blocks.DateTimeBlock(label='Дата события')), ('mesto_sobytiya', wagtail.core.blocks.CharBlock(blank=True, label='Место события', required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(label='Изображение', required=True))], help_text='Укажите дату и время события', icon='fa-calendar', template='blocks/event_block.html'))], blank=True, verbose_name='Основное описание'),
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='date_published',
            field=models.DateField(blank=True, null=True, verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='introduction',
            field=models.TextField(blank=True, help_text='Text to describe the page', verbose_name='Краткое введение'),
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='subtitle',
            field=models.CharField(blank=True, max_length=255, verbose_name='Подзаголовок'),
        ),
    ]
