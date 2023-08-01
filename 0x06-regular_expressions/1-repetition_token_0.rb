#!/usr/bin/env ruby
#regular expression that will match the above cases
puts ARGV[0].scan(/hb{2,5}n/).join
