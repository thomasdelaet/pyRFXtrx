from unittest import TestCase

import RFXtrx


class FanTestCase(TestCase):
    def test_parse_bytes(self):

        fan = RFXtrx.lowlevel.parse(bytearray(b'\x08\x17\x00\x00\x0A\x00\x01\x03\x00'))
        self.assertEqual(fan.__repr__(), "Fan [subtype=0, seqnbr=0, id=0a0001, cmnd=Learn]")
        self.assertEqual(fan.packetlength, 8)
        self.assertEqual(fan.subtype, 0)
        self.assertEqual(fan.type_string, "Siemens SF01")
        self.assertEqual(fan.seqnbr, 0)
        self.assertEqual(fan.id_string, "0a0001")
        self.assertEqual(fan.cmnd, 3)
        self.assertEqual(fan.cmnd_string, "Learn")

        fan = RFXtrx.lowlevel.Fan()
        fan.set_transmit(0, 0, 0x0a0001, 3)
        self.assertEqual(fan.__repr__(), "Fan [subtype=0, seqnbr=0, id=0a0001, cmnd=Learn]")
        self.assertEqual(fan.packetlength, 8)
        self.assertEqual(fan.subtype, 0)
        self.assertEqual(fan.type_string, "Siemens SF01")
        self.assertEqual(fan.seqnbr, 0)
        self.assertEqual(fan.id_string, "0a0001")
        self.assertEqual(fan.cmnd, 3)
        self.assertEqual(fan.cmnd_string, "Learn")

        fan = RFXtrx.lowlevel.Fan()
        fan.parse_id(0, "0a0001")
        self.assertEqual(fan.id_string, "0a0001")
        self.assertEqual(fan.id_combined, 0x0a0001)
        self.assertRaises(ValueError, fan.parse_id, 0, "AA")

        fan = RFXtrx.get_device(0x17, 0, "0a0001")
        self.assertEqual(fan.__str__(), "<class 'RFXtrx.FanDevice'> type='Siemens SF01' id='0a0001'")
        self.assertEqual(fan.id_combined, 0x0a0001)

        fan = RFXtrx.lowlevel.parse(bytearray(b'\x08\x17\x02\x00\x0A\x00\x01\x06\x00'))
        self.assertEqual(fan.cmnd_string, "Unknown command (0x06)")
        self.assertEqual(fan.type_string, "Lucci Air AC")

        fan = RFXtrx.lowlevel.parse(bytearray(b'\x08\x17\x0A\x00\x0A\x00\x01\x05\x00'))
        self.assertEqual(fan.cmnd_string, "Unknown command (0x05)")
        self.assertEqual(fan.type_string, "Unknown type (0x17/0x0a)")

        fan = RFXtrx.get_device(0x17,3,'0a0001')
        self.assertEqual(fan.subtype, 3)
        self.assertEqual(fan.__str__(), "<class 'RFXtrx.FanDevice'> type='SEAV TXS4' id='0a0001'")
