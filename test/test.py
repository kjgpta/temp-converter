from tempcode import tempConverter as conv

def test_fahrToKelv():
    '''
    make sure freezing is calculated correctly
    '''
    
    assert conv(32) == 273.15, 'incorrect freezing point!'