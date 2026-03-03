from sphinx.transforms import SphinxTransform
from sphinx.util import logging
from docutils.nodes import title, section, Text
import re

logger = logging.getLogger(__name__)

class ReplaceInHeaders(SphinxTransform):
    default_priority = 101

    def apply(self):
        counter1 = self.app.env.replace_in_headers_counter1
        counter2 = self.app.env.replace_in_headers_counter2
        for node in self.document.traverse(title):
            if isinstance(node.parent, section):
                text_node = node[0]
                original_text = text_node.astext()
                if "{CHAPTER_LV1}" in original_text:
                    counter1 += 1
                    counter2 = 0
                    new_text = original_text.replace("{CHAPTER_LV1}", f"{str(counter1)}.")
                    new_text_node = Text(new_text)
                    node.replace(text_node, new_text_node)

                if "{CHAPTER_LV2}" in original_text:
                    counter2 += 1
                    new_text = original_text.replace("{CHAPTER_LV2}", f"{str(counter1)}.{str(counter2)}.")
                    new_text_node = Text(new_text)
                    node.replace(text_node, new_text_node)

#                new_text, num_substitutions = re.subn("{CHAPTER_LV1}", f"{str(counter1)}.", original_text)
#                if num_substitutions > 0:
#                    new_text_node = Text(new_text)
#                    node.replace(text_node, new_text_node)
#                    counter1 += 1
#                    counter2 = 1

#                new_text2, num_substitutions2 = re.subn("{CHAPTER_LV2}", f"{str(counter1)}.{str(counter2)}.", original_text)
#                if num_substitutions2 > 0:
#                    new_text_node2 = Text(new_text2)
#                    node.replace(text_node, new_text_node2)
#                    counter2 += 1

#                new_text = re.sub("{CHAPTER_LV1}", str(counter1) + ".", text_node.astext())
#                new_text_node = Text(new_text)
#                node.replace(text_node, new_text_node)

#                counter1 += 1

        self.app.env.replace_in_headers_counter1 = counter1
        self.app.env.replace_in_headers_counter2 = counter2

def setup(app):
    app.add_transform(ReplaceInHeaders)
    app.connect("builder-inited", reset_counter)

def reset_counter(app):
    app.env.replace_in_headers_counter1 = 0
    app.env.replace_in_headers_counter2 = 0
