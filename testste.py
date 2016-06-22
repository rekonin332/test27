
def get_no_of_instances(cls_obj):
    return cls_obj.no_inst


class Kls(object):
    no_inst = 0
    def __init__(self):
        Kls.no_inst = Kls.no_inst + 1


ik1 = Kls()
print(ik1.no_inst)
ik2 = Kls()
print(ik2.no_inst)
ik2 = Kls()

print(get_no_of_instances(ik1))

print 'hello'


# def iget_no_of_instance(ins_obj):
#     return ins_obj.no_inst
# class Kls(object):
#     no_inst = 0
#     def __init__(self):
#         Kls.no_inst = Kls.no_inst + 1
# ik1 = Kls()
# ik2 = Kls()
# print iget_no_of_instance(ik1)
# print iget_no_of_instance(ik2)
