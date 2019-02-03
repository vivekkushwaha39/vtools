import vtools.src.comm.TCPClient as TCPClient


communicator = TCPClient.TCPClient();
communicator.connect('192.168.31.127', 4000)
data = '<DeviceRequest xmlns="http://www.nrf-arts.org/IXRetail/namespace" xmlns:ns2="urn:vfi-viper:eps.2004-03-12" POPID="001" RequestID="00001883" RequestType="Output" WorkstationID="POS001"><Output MaxTime="10" MinTime="10" OutDeviceTarget="PinPad"><TextLine>PARTIALLY APPROVED</TextLine></Output></DeviceRequest>'
communicator.sendMsg(data);

rcv = communicator.recvMsg()

rcvByte = bytearray(0)
rcvByte.extend(rcv[4:])
print(rcvByte)
communicator.disconnect()
