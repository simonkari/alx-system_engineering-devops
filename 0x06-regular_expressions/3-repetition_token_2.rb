#!/usr/bin/env ruby

input = ARGV[0]
matches = input.scan(/hbt+n/)
puts matches.join
