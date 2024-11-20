import xml.etree.ElementTree as ET


def Otstupi(elem, level=0):
    i = "\n" + level * "  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for subelem in elem:
            Otstupi(subelem, level + 1)
        if not subelem.tail or not subelem.tail.strip():
            subelem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i


def save(info, filename):
    root = ET.Element('info')

    classics = ET.SubElement(root, 'classics')
    for classic in info['classics']:
        classic_element = ET.SubElement(classics, 'classic')
        for key, value in classic.items():
            branch = ET.SubElement(classic_element, key)
            branch.text = str(value)

    pops = ET.SubElement(root, 'pops')
    for pop in info['pops']:
        pop_element = ET.SubElement(pops, 'pop')
        for key, value in pop.items():
            branch = ET.SubElement(pop_element, key)
            branch.text = str(value)

    raps = ET.SubElement(root, 'raps')
    for rap in info['reps']:
        rap_element = ET.SubElement(raps, 'rap')
        for key, value in rap.items():
            branch = ET.SubElement(rap_element, key)
            branch.text = str(value)

    Otstupi(root)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def load_from_xml(filename):
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
    except FileNotFoundError:
        return {'classics': [], 'rocks': [], 'pops': [], 'raps': []}

    info = {'classics': [], 'rocks': [], 'pops': [], 'raps': []}

    for classic in root.find('classics'):
        classic_info = {}
        for branch in classic:
            classic_info[branch.tag] = branch.text
        info['classics'].append(classic_info)

    for rock in root.find('rocks'):
        rock_info = {}
        for branch in rock:
            rock_info[branch.tag] = branch.text
        info['rocks'].append(rock_info)

    for pop in root.find('pops'):
        pop_info = {}
        for branch in pop:
            pop_info[branch.tag] = branch.text
        info['pops'].append(pop_info)

    for rap in root.find('raps'):
        rap_info = {}
        for branch in rap:
            rap_info[branch.tag] = branch.text
        info['raps'].append(rap_info)

    return info


def add_classic(info, classic):
    info['classics'].append(classic.to_dict())


def add_rock(info, rok):
    info['rocks'].append(rok.to_dict())


def add_pop(info, pop):
    info['pops'].append(pop.to_dict())


def add_rap(info, rap):
    info['raps'].append(rap.to_dict())


def classic_destruction(info, name):
    space = []
    for classic in info['classics']:
        if classic['name'].lower() != name.lower():
            space.append(classic)

    info['classics'] = space


def rock_destruction(info, name):
    space = []
    for rock in info['rocks']:
        if rock['name'].lower() != name.lower():
            space.append(rock)

    info['rocks'] = space


def pop_destruction(info, name):
    space = []
    for pop in info['pops']:
        if pop['name'].lower() != name.lower():
            space.append(pop)

    info['pops'] = space


def rap_destruction(info, name):
    space = []
    for rap in info['raps']:
        if rap['name'].lower() != name.lower():
            space.append(rap)

    info['raps'] = space