# Please do not edit or delete any file in this folder. Very important
import time

with open (".members.txt", "r") as f:
	data = f.read().split("\n")

template = (
"""
	{
		"pk": "%s",
		"model": "member.member",
		"fields": {
			"name": "%s",
			"address": "%s",
			"post_code": "%s",
			"mobile_no": "%s",
			"email": "%s",
			"first_attended": "2014-09-28",
			"last_modified": "%s",
			"category": "old members",
			"study_place": "%s"
		}"""
)

def write_quote(records):

	with open ("members.json", "w") as fobj:
		fobj.write("[")
		pk = 1
		for record in records:
			last_modified = time.strftime("%Y-%m-%d %H:%m")
			name, address, post_code, number, email = record.split("| ")
			study_place = ""
			
			fobj.write(template % (pk, name, address, post_code, number, email, last_modified, study_place))
			
			if not pk == len(records):
				fobj.write("\n\t},")
			else: fobj.write("\n\t}")
			pk += 1
		fobj.write("\n]")

	print("%s names written successfully" % len(records))

write_quote(data)
print("All operation completed")