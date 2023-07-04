#!/usr/bin/env ruby

input = ARGV[0]
uppercase_letters = input.scan(/[A-Z]/).join
puts uppercase_letters
