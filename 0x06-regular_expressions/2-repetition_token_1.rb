#!/usr/bin/env ruby

input = ARGV[0]
matches = input.scan(/hb?tn/)
puts matches.join
