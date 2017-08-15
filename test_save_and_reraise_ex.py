import six
import sys, traceback


class save_and_reraise_exception(object):
    def __init__(self, reraise=True, logger=None):
        self.reraise = reraise
        self.logger = logger
        self.type_, self.value, self.tb = (None, None, None)

    def force_reraise(self):
        if self.type_ is None and self.value is None:
            raise RuntimeError("There is no (currently) captured exception"
                               " to force the reraising of")
        six.reraise(self.type_, self.value, self.tb)

    def capture(self, check=True):
        (type_, value, tb) = sys.exc_info()
        if check and type_ is None and value is None:
            raise RuntimeError("There is no active exception to capture")
        self.type_, self.value, self.tb = (type_, value, tb)
        return self

    def __enter__(self):
        # TODO(harlowja): perhaps someday in the future turn check here
        # to true, because that is likely the desired intention, and doing
        # so ensures that people are actually using this correctly.
        return self.capture(check=False)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            if self.reraise and self.type_ or self.value or self.tb:
                msg = 'Original exception being dropped: %s' % traceback.format_exception(
                    self.type_, self.value, self.tb)
                print msg
            return not self.reraise
        if self.reraise:
            self.force_reraise()
        else:
            msg = 'exception being dropped: %s' % traceback.format_exception(
                self.type_, self.value, self.tb)
            print msg


with save_and_reraise_exception(reraise=True):
    raise Exception('2')
    print 123
print 456

# try:
#     raise Exception('1')
# except Exception:
#     with save_and_reraise_exception(reraise=True):
#         raise Exception('2')
#         print 123
