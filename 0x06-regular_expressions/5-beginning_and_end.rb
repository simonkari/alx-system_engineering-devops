#!/usr/bin/env ruby

input = ARGV[0]
matches = input.scan(/h.n/)
puts matches.join
