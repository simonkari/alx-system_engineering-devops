#!/usr/bin/env ruby

input = ARGV[0]
matches = input.scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/)
result = matches.join(",")
puts result
