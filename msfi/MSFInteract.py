#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          :
# Author             :
# Date created       :
# Date last modified :
# Python Version     : 3.*

import pexpect, time
import re

class MSFInteract(object):
    """docstring for MSFInteract."""

    def __init__(self, debug=False, debugfilename='debug.log'):
        super(MSFInteract, self).__init__()
        self.debugging_infos = {'status' : debug, 'debugfilename' : debugfilename, 'start_time' : time.time()}
        f = open(self.debugging_infos['debugfilename'], 'w').close() # Clears the debug file
        self._debug("Starting MSFInteract with debugging logs ...")
        self.conn  = {'child' : None, 'status' : False}
        self.connect()

    def connect(self):
        """Documentation for connect"""
        self._debug("Starting msfconsole ...")
        try:
            self.conn = { 'child' : pexpect.spawn("msfconsole"), 'status' : True}
            self._wait_for_prompt()
        except pexpect.exceptions.ExceptionPexpect as e:
            print("[ERROR]",e)
            # pexpect.exceptions.ExceptionPexpect: The command was not found or was not executable: MSFInteract.
        return

    def execute(self, command):
        """Documentation for execute"""
        if self.conn['status'] == True:
            command = self._sanitize(command)
            self._debug("Executing : %s" % command)
            self.conn['child'].send(command+'\n')
            result = self._wait_for_prompt()
            return result
        else :
            return None

    def use(self, exploit):
        if self.conn['status'] == True and len(exploit.strip()) != 0:
            response = self.execute("use "+exploit)
            return response
        else :
            return None

    def exploit(self):
        if self.conn['status'] == True:
            response = self.execute("exploit")
            return response
        else :
            return None

    def search(self, text):
        """Documentation for search"""
        def parse_search(text):
            results = []
            lines   = [l for l in [l.strip() for l in text.split('\n') if len(l.strip()) != 0] if l[0].isdigit()]
            for l in lines :
                l = re.sub(r"[ ]+", " ", l).split(" ")
                entry,k = {'id' : int(l[0]), 'name' : l[1], 'disclosure_date':'', 'rank':'', 'description':''}, 2
                if [s.isdigit() for s in l[k].split('-')] == [True]*3:
                    entry['disclosure_date'], k = l[k], k+1
                if l[k] in ['manual','low','normal','good','great','excellent', 'average']:
                    entry['rank'], k = l[k], k+1
                if l[k] in ['Yes','No']: entry['check'], k = l[k], k+1
                entry['description'] = ' '.join(l[k:])
                results.append(entry)
            return results
        #=======================================================================
        if self.conn['status'] == True:
            self._debug("Search : %s" % text)
            search_results = parse_search(self.execute("search "+text))
            self._debug("Search returned %d entries." % len(search_results))
            return {'results' : search_results}
        else :
            return None

    def set_options(self, options:dict):
        for key in options.keys():
            cmd = ' '.join(["set", str(key), str(options[key])])
            response = self.execute(cmd)
            if bytes(response, "ISO-8859-1") != bytes("\x1b[0m"+str(key)+" => "+str(options[key]), "ISO-8859-1"):
                self._debug("Unexpected response in set_options :")
                self._debug(" ├──> Expeced : "+str(bytes("\x1b[0m"+str(key)+" => "+str(options[key]), "ISO-8859-1")))
                self._debug(" └──> Got     : "+str(bytes(response, "ISO-8859-1")))

    def close(self):
        if self.conn['status'] == True:
            self._debug("Closing MSF Console ...")
            self.conn['child'].send('exit\n')
            self.conn['child'].expect(pexpect.exceptions.EOF)
            self._debug("MSF Console closed.")
            self.conn['status'] = True

    def _debug(self, message):
        if self.debugging_infos['status'] == True :
            running_time = str(round(time.time() - self.debugging_infos['start_time'], 3)).split(".")
            running_time = running_time[0]+'.'+running_time[1].ljust(3,'0')
            print("\x1b[0m\x1b[1m[\x1b[93mDEBUG\x1b[0m:\x1b[95m%s\x1b[0m\x1b[1m]\x1b[0m %s" % (running_time,message))
            f = open(self.debugging_infos['debugfilename'], 'a')
            f.write("[DEBUG:%s] %s" % (running_time,message)+"\n")
            f.close()

# *--------------------------------------------------------------------------- *

    def _wait_for_prompt(self):
        """Documentation for _wait_for_prompt"""
        result = ""
        self.conn['child'].expect([
                r'[\x1b]\[4mmsf5[\x1b]\[0m [\x1b]\[0m>',
                r'[\x1b]\[4mmsf5[\x1b]\[0m [a-zA-Z0-9]*\([\x1b]\[1m[\x1b]\[31m[a-zA-Z0-9_\/\-]*[\x1b]\[0m\) [\x1b]\[0m\>'
            ],
            timeout=-1
        )
        if '\n' in self.conn['child'].before.decode("ISO-8859-1"):
            result += '\n'.join(self.conn['child'].before.decode("ISO-8859-1").split("\n")[1:])
        else :
            result += self.conn['child'].before.decode("ISO-8859-1")
        result = '\n'.join([l.replace('\r','') for l in result.split('\r\n') if len(l.strip()) != 0 and l.strip() != '\x1b[0m'])
        return result

    def _sanitize(self, text):
        """Documentation for _sanitize"""
        stext = text
        if "\n" in stext : stext = stext.split("\n")[0]
        return stext
