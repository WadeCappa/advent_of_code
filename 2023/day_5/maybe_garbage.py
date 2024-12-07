

            print(len(rangesToExplore))
            range = rangesToExplore.pop()
            for r in table.ranges:
                tableRangeStartsFirst = r.source <= range[0]
                tableRangeEndsFirst = r.source + r.size < range[1]
                if r.size + r.source < range[0] or r.source > range[1]:
                    continue
                if tableRangeStartsFirst and not tableRangeEndsFirst:
                    # our range is fully contained
                    newTraversals.append(dfs(tableIndex+1, r.translateInclusiveRange(range)))
                elif tableRangeStartsFirst and tableRangeEndsFirst:
                    print(range, (r.source, r.source+r.size))
                    # our range is both inside and outside of the table's range
                    newTraversals.append(dfs(tableIndex + 1, r.translateInclusiveRange((range[0], r.source + r.size))))
                    rangesToExplore.append((r.source + r.size, range[1]))
                elif not tableRangeStartsFirst and tableRangeEndsFirst:
                    # our range is both inside and outside of the table's range
                    newTraversals.append(dfs(tableIndex+1, r.translateInclusiveRange((r.source, range[1]))))
                    rangesToExplore.append((range[0], r.source))
                elif range[0] < r.size and range[1] > r.source + r.size:
                    # or range is bigger on both sides
                    newTraversals.append(dfs(tableIndex+1, r.translateInclusiveRange((r.source, r.source + r.size))))
                    #rangesToExplore.append((r.source, range[0]))
                    #rangesToExplore.append((range[1], r.source + r.size))