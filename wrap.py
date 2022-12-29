class Wrap(object):

    def __init__(self, obj):
        #self.__data =obj
        self._wrapped_obj = obj
    
    def get(self):
        return self.__data
    
    def __repr__(self):
        return 'self.__data'
    def __str__(self):
        return str(self.__data)
    def __getattr__(self, attr):
        return getattr(self.__data, attr)
    # def __getattr__(self, attr):
    #     #getattr(self.__data, attr)
    # # see if this object has attr
    # # NOTE do not use hasattr, it goes into
    # # infinite recurrsion
    #     if attr in self.__dict__:
    #         # this object has it
    #         return getattr(self, attr)
    #     # proxy to the wrapped object
    #     return getattr(self._wrapped_obj, attr)


#WrapMe(3+3j)

# class Wrapper(object):
#     '''
#     Object wrapper class.
#     This a wrapper for objects. It is initialiesed with the object to wrap
#     and then proxies the unhandled getattribute methods to it.
#     Other classes are to inherit from it.
#     '''
#     def __init__(self, obj):
#         '''
#         Wrapper constructor.
#         @param obj: object to wrap
#         '''
#         # wrap the object
#         self._wrapped_obj = obj

#     def __getattr__(self, attr):
#         # see if this object has attr
#         # NOTE do not use hasattr, it goes into
#         # infinite recurrsion
#         if attr in self.__dict__:
#             # this object has it
#             return getattr(self, attr)
#         # proxy to the wrapped object
#         return getattr(self._wrapped_obj, attr)
