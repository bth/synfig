# pylint: disable=line-too-long
"""
Will store all the functions required for generation of shapeKeyframed file in
lottie
"""

import sys
from properties.shapePropKeyframe.outline import gen_bline_outline
from properties.shapePropKeyframe.region import gen_bline_region
from properties.shapePropKeyframe.polygon import gen_dynamic_list_polygon
from properties.shapePropKeyframe.circle import gen_list_circle
from properties.shapePropKeyframe.rectangle import gen_list_rectangle
from properties.shapePropKeyframe.star import gen_list_star
sys.path.append("../")


def gen_properties_shapeKeyframed(lottie, node, idx):
    """
    Will convert bline points/dynamic_list to bezier points as required by lottie if they are
    animated

    Args:
        lottie      (dict) : Lottie generated shape keyframes will be stored here
        node        (lxml.etree._Element) : Shape/path in Synfig format :- Could be bline_point or dynamic_list
        idx         (int) : Index/Count of shape/path

    Returns:
        (None)
    """
    lottie["ix"] = idx
    lottie["a"] = 1
    lottie["k"] = []
    if node.tag == "layer" and node.attrib["type"] == "circle":
        gen_list_circle(lottie["k"], node)
    elif node.tag == "layer" and node.attrib["type"] in {"rectangle", "filled_rectangle"}:
        gen_list_rectangle(lottie["k"], node)
    elif node.tag == "layer" and node.attrib["type"] == "star":
        gen_list_star(lottie["k"], node)
    elif node.getparent().getparent().attrib["type"] == "region":
        gen_bline_region(lottie["k"], node)
    elif node.getparent().getparent().attrib["type"] == "polygon":
        gen_dynamic_list_polygon(lottie["k"], node)
    elif node.getparent().getparent().attrib["type"] == "outline":
        gen_bline_outline(lottie["k"], node)
