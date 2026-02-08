"""
Invoice Revenue Analyzer
Analyzes PDF invoices to identify top revenue-generating services
"""

import os
from pathlib import Path
from collections import defaultdict
import pdfplumber
from datetime import datetime

def extract_invoice_data(pdf_path):
    """Extract service descriptions and amounts from an invoice PDF"""
    services = []
    
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if not text:
                continue
            
            lines = text.split('\n')
            
            # Find lines between Description header and Subtotal
            in_services_section = False
            for line in lines:
                # Start capturing after Description header
                if 'Description' in line and 'Qty' in line and 'Rate' in line and 'Amount' in line:
                    in_services_section = True
                    continue
                
                # Stop at Subtotal
                if 'Subtotal:' in line or 'Total Due:' in line:
                    in_services_section = False
                    break
                
                # Extract service line
                if in_services_section and line.strip():
                    # Split by multiple spaces to separate description from numbers
                    parts = line.split()
                    
                    # Amount should be the last part (e.g., $1,234.00)
                    if len(parts) >= 2 and parts[-1].startswith('$'):
                        amount_str = parts[-1].replace('$', '').replace(',', '')
                        try:
                            amount = float(amount_str)
                            # Everything except the last 3 parts (hrs, rate, amount) is the description
                            description = ' '.join(parts[:-3])
                            if description:
                                services.append({
                                    'description': description,
                                    'amount': amount,
                                    'invoice': os.path.basename(pdf_path)
                                })
                        except ValueError:
                            continue
    
    return services

def analyze_invoices(invoice_folder, output_file):
    """Analyze all PDF invoices in the specified folder"""
    
    # Collect all services from all invoices
    all_services = []
    invoice_folder = Path(invoice_folder)
    
    # Find all PDF files
    pdf_files = sorted(invoice_folder.glob('*.pdf'))
    
    if not pdf_files:
        msg = f"No PDF files found in {invoice_folder}"
        print(msg)
        with open(output_file, 'w') as f:
            f.write(msg + '\n')
        return
    
    # Open output file for writing
    with open(output_file, 'w') as f:
        # Write header
        f.write(f"Invoice Revenue Analysis Report\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Invoice Folder: {invoice_folder}\n")
        f.write("=" * 80 + "\n\n")
        
        msg = f"Found {len(pdf_files)} PDF invoices"
        print(msg)
        f.write(msg + '\n')
        f.write("=" * 80 + "\n")
        
        # Extract data from each invoice
        for pdf_file in pdf_files:
            services = extract_invoice_data(pdf_file)
            all_services.extend(services)
            msg = f"Processed: {pdf_file.name} - {len(services)} services found"
            print(msg)
            f.write(msg + '\n')
        
        f.write("=" * 80 + "\n\n")
        
        # Aggregate by service description
        service_totals = defaultdict(lambda: {'total': 0.0, 'count': 0, 'invoices': []})
        
        for service in all_services:
            desc = service['description']
            service_totals[desc]['total'] += service['amount']
            service_totals[desc]['count'] += 1
            service_totals[desc]['invoices'].append({
                'invoice': service['invoice'],
                'amount': service['amount']
            })
        
        # Sort by total revenue
        sorted_services = sorted(service_totals.items(), key=lambda x: x[1]['total'], reverse=True)
        
        # Display results
        header = "TOP REVENUE-GENERATING SERVICES"
        print("\n" + header)
        print("=" * 80)
        f.write(header + '\n')
        f.write("=" * 80 + "\n\n")
        
        total_revenue = sum(item[1]['total'] for item in sorted_services)
        
        for i, (service, data) in enumerate(sorted_services, 1):
            percentage = (data['total'] / total_revenue) * 100 if total_revenue > 0 else 0
            
            lines = [
                f"{i}. {service}",
                f"   Total Revenue: ${data['total']:,.2f} ({percentage:.1f}% of total)",
                f"   Occurrences: {data['count']} invoices",
                f"   Average per invoice: ${data['total']/data['count']:,.2f}",
                "",
                "   Breakdown:"
            ]
            
            for line in lines:
                print(line)
                f.write(line + '\n')
            
            # Show breakdown by invoice
            for inv_data in sorted(data['invoices'], key=lambda x: x['amount'], reverse=True):
                line = f"      {inv_data['invoice']}: ${inv_data['amount']:,.2f}"
                print(line)
                f.write(line + '\n')
            
            print()
            f.write('\n')
        
        # Write summary
        summary_lines = [
            "=" * 80,
            f"Total Revenue Across All Invoices: ${total_revenue:,.2f}",
            f"Total Number of Services: {len(all_services)}",
            f"Unique Service Types: {len(service_totals)}"
        ]
        
        for line in summary_lines:
            print(line)
            f.write(line + '\n')
        
        print(f"\nReport saved to: {output_file}")

if __name__ == "__main__":
    # Set your invoice folder path here
    invoice_folder = r"C:\Users\Christian\Documents\Invoices\2026"
    
    # Create output file in the same directory as this script
    script_dir = Path(__file__).parent
    output_file = script_dir / "invoice_analysis_report.txt"
    
    print(f"Analyzing invoices in: {invoice_folder}")
    print(f"Output will be saved to: {output_file}")
    print()
    
    analyze_invoices(invoice_folder, output_file)