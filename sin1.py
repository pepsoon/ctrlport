
import sys
import pmt


from gnuradio.ctrlport.GNURadioControlPortClient import GNURadioControlPortClient

args = sys.argv

hostname = '127.0.0.1'
portnum = 9090
argv = [None, hostname, portnum]
radiosys = GNURadioControlPortClient(argv=argv, rpcmethod='thrift')
radio = radiosys.client

radio.postMessage('copy', 'en', pmt.PMT_T)
radio.postMessage('sig_sour', 'freq', pmt.cons(pmt.intern('freq'), pmt.from_double(100e3)))

sys.exit(1)
