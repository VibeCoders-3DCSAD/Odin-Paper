package main

import (
	"bufio"
	"flag"
	"fmt"
	"os"
	"path/filepath"
	"strings"
)

func main() {
	// --- CLI Flags ---
	folder := flag.String("folder", ".", "Path to the folder containing files to rename")
	prefix := flag.String("prefix", "", "Prefix to add to each filename")
	suffix := flag.String("suffix", "", "Suffix to add before the file extension")
	ext := flag.String("ext", "", "Only rename files with this extension (e.g. .pdf)")
	replace := flag.String("replace", "", "Character(s) to replace in filenames (e.g. ' ')")
	with := flag.String("with", "_", "Replacement character(s) (used with -replace)")
	number := flag.Bool("number", false, "Sequentially number files (e.g. file_01.pdf)")
	dryrun := flag.Bool("dryrun", false, "Preview changes without applying them")
	flag.Parse()

	// Validate folder
	info, err := os.Stat(*folder)
	if err != nil || !info.IsDir() {
		fmt.Printf("Error: '%s' is not a valid directory.\n", *folder)
		os.Exit(1)
	}

	// Collect matching files
	entries, err := os.ReadDir(*folder)
	if err != nil {
		fmt.Printf("Error reading directory: %v\n", err)
		os.Exit(1)
	}

	type renameJob struct {
		oldPath string
		newPath string
	}

	var jobs []renameJob
	counter := 1

	for _, entry := range entries {
		if entry.IsDir() {
			continue
		}

		name := entry.Name()
		fileExt := filepath.Ext(name)
		baseName := strings.TrimSuffix(name, fileExt)

		// Filter by extension if specified
		if *ext != "" && !strings.EqualFold(fileExt, *ext) {
			continue
		}

		newBase := baseName

		// Replace characters
		if *replace != "" {
			newBase = strings.ReplaceAll(newBase, *replace, *with)
		}

		// Add prefix
		if *prefix != "" {
			newBase = *prefix + newBase
		}

		// Add suffix (before extension)
		if *suffix != "" {
			newBase = newBase + *suffix
		}

		// Sequential numbering
		if *number {
			newBase = fmt.Sprintf("%s_%02d", newBase, counter)
			counter++
		}

		newName := newBase + fileExt
		oldPath := filepath.Join(*folder, name)
		newPath := filepath.Join(*folder, newName)

		// Skip if nothing changed
		if name == newName {
			continue
		}

		jobs = append(jobs, renameJob{oldPath: oldPath, newPath: newPath})
	}

	if len(jobs) == 0 {
		fmt.Println("No files matched or no changes would be made.")
		return
	}

	// Show preview
	fmt.Printf("\n%d file(s) will be renamed:\n\n", len(jobs))
	for _, job := range jobs {
		fmt.Printf("  %-40s  →  %s\n",
			filepath.Base(job.oldPath),
			filepath.Base(job.newPath),
		)
	}

	if *dryrun {
		fmt.Println("\n[Dry run] No changes were applied.")
		return
	}

	// Confirm
	fmt.Print("\nApply changes? (y/N): ")
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	input := strings.TrimSpace(strings.ToLower(scanner.Text()))

	if input != "y" {
		fmt.Println("Cancelled. No files were renamed.")
		return
	}

	// Apply renames
	successCount := 0
	for _, job := range jobs {
		if err := os.Rename(job.oldPath, job.newPath); err != nil {
			fmt.Printf("  Error renaming '%s': %v\n", filepath.Base(job.oldPath), err)
		} else {
			fmt.Printf("  Renamed: %s\n", filepath.Base(job.newPath))
			successCount++
		}
	}

	fmt.Printf("\nDone. %d/%d file(s) renamed successfully.\n", successCount, len(jobs))
}