# Generated by Django 2.1.4 on 2018-12-16 11:39

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20181216_0143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='body',
            field=wagtail.core.fields.StreamField([('heading_block', wagtail.core.blocks.StructBlock([('heading_text', wagtail.core.blocks.CharBlock(classname='title', required=True)), ('size', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4')], required=False))])), ('paragraph_block', wagtail.core.blocks.RichTextBlock(icon='fa-paragraph', template='blocks/paragraph_block.html')), ('image_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False))])), ('block_quote', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.TextBlock()), ('attribute_name', wagtail.core.blocks.CharBlock(blank=True, label='e.g. Mary Berry', required=False))])), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='fa-s15', template='blocks/embed_block.html')), ('event_block', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(blank=True, label='концерт Black Sabbath', required=False)), ('age_policy', wagtail.core.blocks.IntegerBlock(help_text='Возрастной контроль', max_value=18, min_value=0)), ('event_time', wagtail.core.blocks.DateTimeBlock(help_text='Дата и время события')), ('image', wagtail.images.blocks.ImageChooserBlock(required=True))], help_text='Укажите дату и время события', icon='fa-calendar-alt', template='blocks/event_block.html'))], blank=True, verbose_name='Page body'),
        ),
    ]
