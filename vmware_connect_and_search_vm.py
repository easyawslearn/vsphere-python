from pyVim import connect
import sys

my_cluster = connect.ConnectNoSSL(sys.argv[1], 443, sys.argv[2], sys.argv[3])

searcher = my_cluster.content.searchIndex
vm = searcher.FindByIp(ip=sys.argv[4], vmSearch=True)
print vm.config.name

connect.Disconnect(my_cluster)
