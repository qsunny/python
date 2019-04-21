
from .base_dao import Component,ComponentProps
from .base_dao import Session
from com.aaron.bean.component_property import ComponentProperty
from com.aaron.bean.component_prop import ComponentProp


def addComponent(componentProperty):
    '''添加component'''
    if(componentProperty is None):
        return 0;
    # 创建session对象:
    session = Session()
    propList = componentProperty.getPropList()
    component = Component(category1=componentProperty.category1,category2=componentProperty.category2,
                          category3=componentProperty.category3,category4=componentProperty.category4,category_type_num=componentProperty.categoryTypeNum)
    session.add(component)
    session.commit()

    session.refresh(component)
    session.expunge(component)

    session.close()
    print("======")
    print(component)

    # 添加属性列表
    addComponentProps(componentProperty,component)

def addComponentProps(componentProperty,component):
    '''添加component prop list'''
    if(componentProperty is None):
        return 0;

    propList = componentProperty.getPropList()

    component_list = []

    if propList is not None:
        for prop in propList:
            cp = ComponentProps(prop_name=prop.propName,prop_value=prop.propValue,category_type_num=component.category_type_num,component_id=component.id)
            component_list.append(cp)

    if component_list is not None:
        # 创建session对象:
        session = Session()
        session.add_all(component_list)
        session.commit()
        session.close()