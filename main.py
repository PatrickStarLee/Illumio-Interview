# parse through lookup-tbl.txt (lookup table file) and store {(dstport, protcol) : tag} as a key-value pair in lookup
def parse_lookup(lookup, lookup_tbl):
    with open(lookup_tbl, "r") as file:
        content = file.read()
        lines = content.split("\n")
        for l in lines:
            dstport, protocol, tag = l.split(",")
            lookup[(dstport, protocol)] = tag

# parse through protocol-numbers-1.csv and store {decimal : protocol} as a key-value pair in protocols
def parse_protocols(protocols):
    with open("protocol-numbers-1.csv", "r") as file:
        content = file.read()
        lines = content.split("\n")
        for l in lines:
            info = l.split(",") # information in each log is split into an array
            decimal, protocol = info[0], info[1]
            
            if decimal == "146-252":
                for d in range(146, 253):
                    protocols[str(d)] = protocol
            else:
                protocols[decimal] = protocol

# main program
def main():
    lookup_map = {}
    protocols_map = {}
    
    flowlogs_file = input("Enter name of flow logs filename: ")
    lookup_tbl = input("Enter lookup table filename: ")

    parse_lookup(lookup_map, lookup_tbl)
    parse_protocols(protocols_map)

    # dictionary for tag_count where { tag : count } is a key value pair
    tag_count = {}
    
    # dictionary for port/protocol count where { (dstport, protocol) : count } is a key value pair
    port_protocol_count = {}

    # parse the flow logs from flowlogs.txt and store in logs
    with open(flowlogs_file, "r") as file:
        content = file.read()
        logs = content.split("\n")
        for l in logs:
            info = l.split(" ") # information in each log is split into an array

            # indices where fields are located (array format where 0 is starting index)
            # 6 - dstport
            # 7 - protocol
            tmp_tuple = (info[6], protocols_map[info[7]].lower())
        
            # for tag_count
            if tmp_tuple not in lookup_map:
                tag_count['Untagged'] = 1 + tag_count.get('Untagged', 0)
            else:
                dec_to_protocol = lookup_map[tmp_tuple]
                tag_count[dec_to_protocol] = 1 + tag_count.get(dec_to_protocol, 0)
            
            # for port_protocol_count
            port_protocol_count[(tmp_tuple)] = 1 + port_protocol_count.get(tmp_tuple, 0)

    file = open("output.txt", "w")
    file.write("Tag Counts:\n\nTag,Count\n")
    for t in tag_count:
        file.write(str(t) + "," + str(tag_count[t]) + '\n')

    file.write('\nPort/Protocol Combination Counts:\n\nPort,Protocol,Count\n')
    for p in port_protocol_count:
        file.write(str(p[0]) + "," + str(p[1]) + "," + str(port_protocol_count[p]) + "\n")

    file.close()

main()