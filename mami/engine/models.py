from django.db import models

class Stream(models.Model):
    protocol = models.CharField(max_length=4, blank=False, null=False, default='http')
    ip = models.GenericIPAddressField(protocol='both', unpack_ipv4=True, blank=False, null=False, default='127.0.0.1')
    port = models.SmallIntegerField(blank=False, null=False, default='80')
    
    name = models.TextField(blank=True, null=True)
    IPTV = 0
    OTT = 1
    SAT = 2
    BROADCAST_TYPES = (
        (IPTV, 'IPTV'),
        (OTT, 'OTT'),
        (SAT, 'SAT'),
    )
    broadcast_type = models.IntegerField(default=IPTV, choices=BROADCAST_TYPES)

    def get_url(self):
        return string(self.protocol) + '://' + string(self.ip) + ':' + string(self.port)


class Multiview(models.Model):
    name = models.TextField(blank=False, null=False, default='Unnamed Multiview')
    stream_list = models.ManyToManyField(Stream, related_name='stream_list')

    def get_broadcast_type_list(self):
        broadcast_type_list = []
        for stream in self.stream_list.all():
            if stream.broadcast_type not in broadcast_type_list:
                broadcast_type_list.append(stream.broadcast_type)
        return broadcast_type_list

