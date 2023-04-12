from .aircraft import Aircraft
from .cub import CUB
from .dogs import Dogs


def get_trainval_datasets(tag, resize):
    if tag == 'aircraft':
        return Aircraft(phase='train', resize=resize), Aircraft(phase='val', resize=resize)
    elif tag == 'bird':
        return CUB(phase='train', resize=resize), cub(phase='val', resize=resize)
    elif tag == 'car':
        return Dogs(phase='train', resize=resize), Dogs(phase='val', resize=resize)
    else:
        raise ValueError('Unsupported Tag {}'.format(tag))